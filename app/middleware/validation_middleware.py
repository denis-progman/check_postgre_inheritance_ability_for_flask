import re
from exceptions.validation_error import ValidationError


class ValidationMiddleware:
    VALIDATION_RULES_KEY = "validation"

    # Validator keys
    HTTP_CODE = "http_code"
    ERROR_MESSAGE = "message"
    VALIDATION_FUNCTION = "validator"

    # Validators
    IS_REQUIRED = "is_required"
    IS_NULLABLE = "is_nullable"
    REGEXP_PATTERN = "pattern"

    # Validation configuration
    FIELD_VALIDATORS = {
        IS_REQUIRED: {
            HTTP_CODE: 400,
            ERROR_MESSAGE: "Field '{field}' is required",
            VALIDATION_FUNCTION: lambda field_name, field_rules, data: field_name in data
        },
        IS_NULLABLE: {
            HTTP_CODE: 400,
            ERROR_MESSAGE: "Field '{field}' cannot be empty",
            VALIDATION_FUNCTION: lambda field_name, field_rules, data: (
                data.get(field_name) or field_rules.get(ValidationMiddleware.IS_NULLABLE, True)
            )
        },
        REGEXP_PATTERN: {
            HTTP_CODE: 400,
            ERROR_MESSAGE: "Field '{field}' does not match the pattern '{pattern}'",
            VALIDATION_FUNCTION: lambda field_name, field_rules, data: ValidationMiddleware._validate_regexp(
                field_name, field_rules, data
            )
        },
    }

    def __init__(self, router_rules):
        self.router_rules = {rule["rule"]: rule for rule in router_rules}

    def process_request(self, rule, request):
        """Main process method to validate the request."""
        route_config = self.router_rules.get(rule)
        if not route_config or ValidationMiddleware.VALIDATION_RULES_KEY not in route_config:
            return None  # No validation needed for this route

        validation_config = route_config[ValidationMiddleware.VALIDATION_RULES_KEY]

        # Validate fields
        fields = validation_config.get("fields", {})
        for field_name, field_rules in fields.items():
            for validator_name, validator_config in self.FIELD_VALIDATORS.items():
                if validator_name in field_rules:
                    try:
                        is_valid = validator_config[ValidationMiddleware.VALIDATION_FUNCTION](
                            field_name, field_rules, request.json
                        )
                        if not is_valid:
                            return self._create_error_response(validator_name, field_name, field_rules)
                    except KeyError as e:
                        raise ValidationError(
                            f"Validation rule '{validator_name}' for field '{field_name}' "
                            f"requires missing key: '{e.args[0]}'."
                        )
                    except ValidationError as ve:
                        return {"error": str(ve)}, 400

        return None  # No validation errors

    def _create_error_response(self, validator_name, field_name, field_rules):
        """Generate an error response based on the validation failure."""
        validator_config = self.FIELD_VALIDATORS[validator_name]
        try:
            message = validator_config[self.ERROR_MESSAGE].format(
                field=field_name, **field_rules
            )
        except KeyError as e:
            missing_key = e.args[0]
            message = (
                f"Validation failed for field '{field_name}': Missing key '{missing_key}' "
                f"in field rules."
            )

        return {"error": message}, validator_config[self.HTTP_CODE]

    @staticmethod
    def _validate_regexp(field_name, field_rules, data):
        """Check if the field matches the regexp."""
        value = data.get(field_name)
        pattern = field_rules.get(ValidationMiddleware.REGEXP_PATTERN)

        # If no pattern is provided, skip the validation
        if not pattern:
            return True

        try:
            # Compile the pattern to validate its correctness
            compiled_pattern = re.compile(pattern)
        except re.error:
            # Raise an error for invalid patterns
            raise ValidationError(
                f"Invalid regexp pattern for field '{field_name}': {pattern}"
            )

        # Match the pattern against the value
        return bool(compiled_pattern.fullmatch(str(value)))
