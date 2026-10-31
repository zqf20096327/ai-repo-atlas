# ConardLi/easy-agent

⭐ 1,018 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ConardLi/easy-agent) · 个人维护 · 中文 README

**终端编程 agent：读改代码、跑命令，受权限与沙箱约束**

运行在终端旁仓库目录中的编程 agent（eagent）：接收任务后规划、读写文件、运行测试与 shell 命令并汇报。所有可变更机器的操作经过 allow/ask/deny 权限规则、工作区信任与可选 OS 级沙箱（macOS Seatbelt、Linux bubblewrap）。支持 Anthropic、OpenAI 兼容、Gemini 与本地模型。代码分层组织（模型通信、agent 循环、工具、权限、上下文），附学习路径文档。通过 npm 全局安装或 npx 直接运行，需 Node.js 22+。扩展机制含 MCP、skills、子 agent、hooks 与插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- allow/ask/deny 权限规则 + 工作区信任 + OS 级沙箱（Seatbelt/bubblewrap）多层安全模型
- 支持 Anthropic、OpenAI 兼容、Gemini 与本地模型，多 profile 配置
- MCP、skills、子 agent、hooks、插件等扩展体系
- headless JSON/NDJSON 输出、JSON-RPC 与 Agent Client Protocol 供 IDE 等外部程序接入

## 适用场景

- 在终端里让 agent 理解陌生代码库并解释流程
- 多文件修改后审查 diff，必要时 /rewind 撤销
- 先在只读 Plan Mode 规划变更再执行
- 在 CI 或脚本中以管道方式调用并读取结构化输出

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A terminal coding agent that reads your code, edits files, and runs commands under permission rules you control.
> L7: Easy Agent (`eagent`) runs in your terminal next to your repository. Describe a task and it plans the work, reads an

## 星数曲线

```mermaid
xychart-beta
    title "ConardLi/easy-agent 星数(近 6 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26", "2026-10-28", "2026-10-29", "2026-10-31"]
    y-axis "stars" 1014 --> 1019
    line [1015, 1016, 1015, 1016, 1018, 1018]
```

2026-10-18 1,015 → 2026-10-31 1,018（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d59bc11d162a` · [字段定义](../../DATASET.md)*
