class CreatePlayers < ActiveRecord::Migration[7.2]
  def change
    create_table :players do |t|
      t.integer :tID
      t.string :key

      t.timestamps
    end
    add_index :players, :tID, unique: true
  end
end
