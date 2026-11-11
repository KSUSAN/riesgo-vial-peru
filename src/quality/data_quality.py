def validate_nulls(df):

    null_count = df.isnull().sum().sum()

    print(
        f"Nulos encontrados: {null_count}"
    )

    return null_count


def validate_duplicates(df):

    duplicates = df.duplicated().sum()

    print(
        f"Duplicados encontrados: {duplicates}"
    )

    return duplicates
