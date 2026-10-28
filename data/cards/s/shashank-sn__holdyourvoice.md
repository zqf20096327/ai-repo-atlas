# shashank-sn/holdyourvoice

⭐ 32 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/shashank-sn/holdyourvoice) · 个人维护

**本地校验写作风格的 CLI/MCP 工具，保作者声线于 AI 编辑**

面向与 AI 协作的写作者的本地检查工具：从用户的写作样本构建 voice profile，对比草稿的句式、节奏、词汇与标点；对 AI 编辑后的候选稿执行验证，标记泛化措辞、核验事实声明与来源文件、检测隐藏 Unicode 字符并做交付前门禁。自身不调用模型、无需账号或 API key，通过 CLI、MCP server 与可移植 agent 契约使用；编辑交由用户选择的编辑器或模型完成。需要 Node.js 20+，所有数据留在本地。

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

- 基于本地样本的 voice profile 比对（句式/节奏/词汇/标点）
- 对编辑候选稿执行 verify 与 final-check 门禁（隐藏字符未解决则退出码 2）
- fact-lint/logic-lint 依据本地来源文件核验声明与文档逻辑
- 提供 MCP server 与 agent 契约（skills/hyv-*），无运行时网络请求

## 适用场景

- 用 AI 改写文稿后，校验修改是否保留了我的写作风格
- 发布前检测草稿中的泛化 AI 措辞与隐藏字符
- 让 Claude/Codex 等 agent 通过 MCP 调用同一套本地检查

## 场景标签

 · 领域:写作/文本校验工具

## 证据(README 行号)

> L7: hold your voice (`hyv`) checks writing locally. it compares a draft with your writing samples, flags generic writing
> L9: it works through a command-line tool, an mcp server, and portable agent contracts. it needs node.js 20 or newer. it 
> L107: ## use with an agent

## 星数曲线

```mermaid
xychart-beta
    title "shashank-sn/holdyourvoice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b6cc26aa7944` · [字段定义](../../DATASET.md)*
