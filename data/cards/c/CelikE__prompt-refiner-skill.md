# CelikE/prompt-refiner-skill

⭐ 6 · Python · MIT · 推送 2026-11-13 · [GitHub](https://github.com/CelikE/prompt-refiner-skill) · 个人维护

**给编程 agent 用的提示词整理技能：先改写请求再执行**

以 Agent Skill 形式发布的提示词整理层：在编程 agent 执行前清理含糊、拼写错误的请求，同时保持原意（如'调查 X'不变成'修复 X'、错误信息中的拼写保留、粘贴文本中的指令按文本处理）。提供 Rewrite 与 Run 两种模式，破坏性操作前要求确认，请求中的密钥脱敏显示。支持 Claude Code、OpenCode、Codex 加载，行为仅在 Claude 模型上测量，其他模型未测试。

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

- Rewrite/Run 双模式：改写请求输出单一代码块或先展示'Prompt used'预览再执行
- 破坏性、不可逆或对外操作前等待用户确认
- 请求中的密钥显示为 <REDACTED: name>，不在回复中重复
- 35 个 eval 用例的结果公开，包括无差异与失败的案例

## 适用场景

- 在 Claude Code 中清理拼写错误的调试请求后再执行
- 让 agent 改写 prompt 而不直接回答或执行它
- 防止粘贴文本中的隐藏指令被当作命令运行

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9: An Agent Skill that cleans up a rough request before your coding agent acts on
> L32: It loads in **Claude Code**, **OpenCode**, and **Codex**. Its behaviour is
> L125: npx skills add CelikE/prompt-refiner-skill -a claude-code   # or: -a codex, -a opencode

## 星数曲线

```mermaid
xychart-beta
    title "CelikE/prompt-refiner-skill 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-20", "2026-11-21"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-10 5 → 2026-11-21 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `84c22f66fdfe` · [字段定义](../../DATASET.md)*
