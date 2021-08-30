class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = []
        new_dict = {}
        for item in cpdomains:
            count, domain = item.split()
            frags = domain.split(".")
            last = frags[-1]
            if last in new_dict:
                new_dict[last] += int(count)
            else:
                new_dict[last] = int(count)
            for i in range(len(frags) - 2, -1, -1):
                last = frags[i] + "." + last
                if last in new_dict:
                    new_dict[last] += int(count)
                else:
                    new_dict[last] = int(count)

        for key,val in new_dict.items():
            output.append(str(val) + " " + key)
        return output