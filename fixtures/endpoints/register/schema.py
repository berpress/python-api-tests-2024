from schema import Schema, And, Use, Optional, SchemaError

REGISTER_SCHEMA = Schema(
        {
            "message": str,
            "uuid": int,
        }
)