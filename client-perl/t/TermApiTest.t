=begin comment

sts

This is the API for metamodel database

The version of the OpenAPI document: 1.0.0
Contact: mark.benson@nih.gov
Generated by: https://openapi-generator.tech

=end comment

=cut

#
# NOTE: This class is auto generated by OpenAPI Generator
# Please update the test cases below to test the API endpoints.
# Ref: https://openapi-generator.tech
#
use Test::More tests => 1; #TODO update number of test cases
use Test::Exception;

use lib 'lib';
use strict;
use warnings;

use_ok('WWW::OpenAPIClient::TermApi');

my $api = WWW::OpenAPIClient::TermApi->new();
isa_ok($api, 'WWW::OpenAPIClient::TermApi');

#
# get_list_of_terms test
#
{
    my $result = $api->get_list_of_terms();
}

#
# get_termy_by_id test
#
{
    my $term_id = undef; # replace NULL with a proper value
    my $result = $api->get_termy_by_id(term_id => $term_id);
}


1;
