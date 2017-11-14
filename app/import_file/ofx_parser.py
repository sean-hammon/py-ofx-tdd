

class OfxParser:

    def __init__(self, contents):
        self.lines = contents

    def get_token(self, line, start):
        if line[start] == '<':

            #   We're looking at a tag, we need to find the end
            #   of the tag.

            end = line.find('>', start) + 1
        else:

            #   We're looking at a value, we need to find
            #   the beginning of the next tag.

            end = line.find('<', start)

        token = line[start:end]
        return [end, token]

