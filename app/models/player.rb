# == Schema Information
#
# Table name: players
#
#  id         :bigint           not null, primary key
#  key        :string
#  tID        :integer
#  created_at :datetime         not null
#  updated_at :datetime         not null
#
# Indexes
#
#  index_players_on_tID  (tID) UNIQUE
#
class Player < ApplicationRecord
end
