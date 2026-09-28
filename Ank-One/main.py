from app.eda.eda import DatasetEDA
from app.data_split.splitter import DatasetSplitter


def main():

    eda = DatasetEDA()

    df = eda.load_dataset()

    eda.basic_information(df)

    df = eda.clean_dataset(df)

    df = eda.sentence_length(df)

    eda.plot_sentence_length(df)

    splitter = DatasetSplitter()

    train_df, validation_df, test_df = splitter.split(df)

    splitter.save(train_df, validation_df, test_df)


if __name__ == "__main__":
    main()