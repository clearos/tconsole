#ifndef _UTIL_H
#define _UTIL_H

#include <sys/types.h>
#include <sys/stat.h>

#include <regex.h>

#ifndef LAN_IP_REFRESH_INT
#define LAN_IP_REFRESH_INT       15
#endif

#define _(STRING) gettext(STRING)

using namespace std;

class ccRegEx
{
public:
    ccRegEx(const char *expr, size_t nmatch = 0, int flags = REG_EXTENDED);
    ~ccRegEx();

    int Execute(const char *subject);
    const char *GetMatch(size_t match);

    void Error(int rc, ostringstream &os);

protected:
    regex_t regex;
    size_t nmatch;
    regmatch_t *match;
    char **matches;
};

class ccFile
{
public:
    ccFile();
    ccFile(const char *filename);
    ~ccFile();

    const char *Map(const char *filename);
    const char *Read(const char *filename);
    const char *GetBuffer(void) { return buffer; };

protected:
    void Reset(void);

    int fd;
    const char *filename;
    char *buffer;
    struct stat file_stat;
};

void ccGetLanIp(const char *command, string &ip);

#endif // _UTIL_H
// vi: ts=4
