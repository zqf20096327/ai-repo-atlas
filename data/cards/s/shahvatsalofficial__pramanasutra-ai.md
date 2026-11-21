# shahvatsalofficial/pramanasutra-ai

⭐ 4 · HTML · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/shahvatsalofficial/pramanasutra-ai) · [官网](https://shahvatsalofficial.github.io/pramanasutra-ai/) · 个人维护

**面向编码 agent 的 QA 与发布门禁 agent，产出证据式审计报告**

为 Claude Code、Cursor、Codex、GitHub Copilot 与 Gemini CLI 提供 17 个可移植 Agent Skills，并附带一个离线确定性 CLI。CLI 读取仓库、不运行测试，生成 report.md/html/json/sarif 四种格式的审计报告，静态发现以 file:line 引证；发布门禁输出 NO_GO、REVIEW_REQUIRED 或 READY_FOR_HUMAN_APPROVAL 三种判定，即使 ready 仍需人工批准。CLI 零运行时依赖、无网络调用、无需额外 API key，Skills 复用宿主 IDE 自带模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个 Agent Skills（PramanaSutra Prime 领衔），适配 5 种 IDE 的技能目录路径
- 离线 CLI 生成 Markdown/HTML/JSON/SARIF 四格式审计报告，发现带 file:line 引证
- 发布门禁三态判定，ready 结果仍要求人工批准，自动部署标记为 false
- 零运行时依赖、无网络调用、无需额外 API key

## 适用场景

- 在 PR 审查中获得带 file:line 证据的测试质量静态审计
- 用门禁命令把发布决策固化为 NO_GO/READY 等可退出码的判定
- 向 Claude Code/Cursor 等 IDE agent 安装 QA 类技能工作流
- 在 CI 中生成 SARIF 报告供流水线消费

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: QA and release-readiness agent for Claude Code, Cursor, Codex, GitHub Copilot and Gemini CLI.
> L16: PramanaSutra AI (from *pramana*, "valid proof") is an open-source **QA and release-readiness agent**. It ships 17 p
> L20: > **No extra API key.** Skills use the IDE's own model. The CLI makes no network calls and has no telemetry.

## 星数曲线

```mermaid
xychart-beta
    title "shahvatsalofficial/pramanasutra-ai 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-21"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-16 4 → 2026-11-21 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a98031c6158c` · [字段定义](../../DATASET.md)*
