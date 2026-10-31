# atxp-dev/atxp

⭐ 45 · TypeScript · MIT · 推送 2026-03-03 · [GitHub](https://github.com/atxp-dev/atxp) · [官网](https://atxp.ai) · 组织维护

**给 AI agent 提供钱包/邮箱/电话与付费 MCP 工具的支付基础设施**

ATXP（Agent Transaction Protocol）以标准 MCP 服务器形式运行，让 AI agent 无需自行管理 API key 即可按用量付费使用工具：41 个常驻工具覆盖网页/X 搜索、图片/视频/音乐生成、@atxp.email 邮箱、短信与语音通话、子 agent 管理等；Gemini CLI 扩展另有浏览、爬取、沙箱代码执行与云文件存储等远程工具。agent 可通过 atxp_register 工具自注册，即时获得 10 个 IOU 代币、独立邮箱与以太坊钱包。计费以 USDC 按次结算，兼容 Gemini CLI、Claude Desktop、Cursor、Windsurf 及任意 MCP 客户端，通过 npx 或扩展方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 MCP 服务器（stdio）形式提供 41 个常驻工具
- agent 自注册即获邮箱、以太坊钱包与 10 个 IOU 代币
- USDC 按次计费，无需管理各服务 API key
- Gemini CLI 扩展提供沙箱代码执行、网页爬取等远程工具

## 适用场景

- 让我的 agent 自主执行搜索、媒体生成、发短信等付费任务
- 为 agent 配备独立邮箱与电话号码用于对外沟通
- 在沙箱中让 agent 执行代码并存储文件

## 场景标签

`图像生成` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: ATXP (Agent Transaction Protocol) lets AI agents pay for their own tools and services without managing API keys. Sel
> L34: ATXP runs as a standard MCP server over stdio. Point any MCP-compatible client at the command above.

## 星数曲线

```mermaid
xychart-beta
    title "atxp-dev/atxp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2e416ce3de40` · [字段定义](../../DATASET.md)*
