# apex-engine-dev/apex-verify

⭐ 4 · JavaScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/apex-engine-dev/apex-verify) · [官网](https://dev.to/amit_spitzer/are-ai-written-tests-really-tests-what-the-research-says-and-what-happened-when-we-tested-it-4ph5) · 个人维护

**用另一个 AI 为 AI 代码改动补写缺失检查并给出 ready/not ready 判定的 CLI**

面向使用 AI 编码工具的开发者的验证工具：从任务文本（而非 agent 自己的测试）生成缺失检查，先在旧代码上运行以证明其能区分新旧，再给出 ready/not ready/unknown 判定与证据。同时扫描测试作弊行为（删除/跳过测试、弱化断言），一切在沙箱副本中运行。无 API key 时复用已登录的 Claude Code/Gemini CLI，有 key 时直连 API；以 npx CLI、Claude Code/Gemini CLI hook、GitHub Action、MCP 工具形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从任务文本生成缺失检查并在旧代码上验证其可失败性
- 支持沙箱运行（macOS Seatbelt/Linux bubblewrap/Windows AppContainer）
- 测试作弊扫描：删除、跳过、.only、断言弱化等
- 支持 node:test、pytest、Jest、Vitest、cargo test、go test 六种测试框架

## 适用场景

- 在 Claude Code 或 Gemini CLI 会话中拦截未真正完成的 'done'
- 在 GitHub PR 上以 Action 评论形式给出判定
- 审查 agent 对 working tree、分支或任意 diff 的改动

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L4:  Catch the AI code changes that pass your tests and are still wrong. A different AI writes the checks your tests are
> L31: **No API key needed.** If you have **Claude Code** or **Gemini CLI** signed in, Apex verify uses it to write the ch
> L71: |**Claude Code**|`/plugin marketplace add apex-engine-dev/apex-verify` then `/plugin install apex-verify@apex`: a S

## 星数曲线

```mermaid
xychart-beta
    title "apex-engine-dev/apex-verify 星数(近 3 点)"
    x-axis ["2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-26 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `26544f6d7bad` · [字段定义](../../DATASET.md)*
