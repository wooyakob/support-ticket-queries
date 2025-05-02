-- Create index on first element (price) of Product Price array
CREATE INDEX idx_product_price_first ON `us-customers`(`Product Price`[0]);