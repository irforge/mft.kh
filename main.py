import fixtures
import outputs
import process


def main() -> None:
    outputs.show_message(fixtures.welcome_message)
    process.run_calculator()
    outputs.show_message(fixtures.goodbye_message)


if __name__ == "__main__":
    main()
