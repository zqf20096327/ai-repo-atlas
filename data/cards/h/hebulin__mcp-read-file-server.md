# hebulin/mcp-read-file-server

⭐ 14 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/hebulin/mcp-read-file-server) · 个人维护 · 中文 README

**加密环境下供 AI Agent 明文读写文件的 MCP 工具服务**

面向使用透明加密软件（天锐绿盾、IP-Guard 等）的企业开发者的 MCP Server：当 Node.js 进程被加密软件列为白名单时，通过 fs 模块为 AI Agent（Claude Code、Cursor、Cline 等）提供替代内置工具的 18 个文件读写/搜索/复制移动工具，解决 Agent 读到密文的问题。关键机制包括目录级加密探测、writePolicy 写入策略、可回滚的事务提交、跨实例路径锁与安全中转校验；前提是 Node.js 必须在白名单内，外部读取器目前仅支持 Windows PowerShell。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个 MCP 文件工具（读写、编辑、搜索、复制/移动/删除、策略诊断）
- 目录级加密探测与 auto/preserve/plaintext 三种写入策略
- 暂存→备份→rename→终验的可回滚事务提交与跨实例路径锁
- 以 npm 包形式通过 npx 运行，遵循标准 MCP 协议

## 适用场景

- 公司装了透明加密软件，AI Agent 编码助手只能读到密文时替代其内置文件工具
- 在加密环境中让 Agent 安全地编辑、复制、移动项目文件
- 通过 MCP_READ_ONLY / MCP_ALLOWED_ROOTS 限制 Agent 的文件操作范围

## 场景标签

 · 领域:AI Agent 工具链/文件系统

## 证据(README 行号)

> L5: 加密环境文件操作工具。当 Node.js 是加密软件白名单进程时，通过 fs 模块自动解密读写文件明文，替代 AI Agent 内置文件工具，解决加密环境下读到密文的问题。适用于任何支持 MCP 协议的 AI Agent。
> L30: 电脑安装了文件加密软件（如天锐绿盾、IP-Guard、亿赛通、深信服等），磁盘上的文件是密文。AI Agent（Claude Code、Cursor、Windsurf、Cline 等）是独立进程，内置文件工具不在白名单内，只能读到
> L51: AI Agent  --(MCP/stdio)-->  Node.js MCP Server(index.js)  --(lib/ 模块)-->  fs 读写明文

## 星数曲线

```mermaid
xychart-beta
    title "hebulin/mcp-read-file-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c004ee5f4d70` · [字段定义](../../DATASET.md)*
