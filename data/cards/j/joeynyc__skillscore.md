# joeynyc/skillscore

⭐ 18 · TypeScript · MIT · 推送 2026-04-22 · [GitHub](https://github.com/joeynyc/skillscore) · 个人维护

**AI agent 技能（SKILL.md）质量评分 CLI 工具**

TypeScript 编写的命令行工具，对 SKILL.md 格式的 AI agent 技能进行质量评估：按对齐 Anthropic 官方技能文档的 7 个加权类别（标识与元数据、简洁性、清晰度、路由与范围、健壮性、安全、可移植性）打分并给出 A+ 到 F 等级与具体发现。支持从 skills.sh、ClawHub、GitHub 仓库或本地目录读取技能，输出终端彩色、JSON、Markdown 三种报告，支持批量对比模式。评分为确定性分析，无需 API key；也可作为 Node.js 库编程调用。

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

- 7 个 Anthropic 对齐加权类别的确定性评分，无需 API key
- 支持 GitHub 仓库、本地目录与批量对比模式
- 终端/JSON/Markdown 三种输出格式
- 提供 Node.js API（SkillParser/SkillScorer/三种 Reporter）

## 适用场景

- 发布前检查自己编写的 agent 技能是否符合规范
- 批量评估并对比多个技能的质量得分
- 在 CI 或脚本中用 JSON 输出集成质量检查

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8:  **The universal quality standard for AI agent skills.**
> L126: SkillScore evaluates skills across **7 weighted categories** aligned with Anthropic's official skill documentation

## 星数曲线

```mermaid
xychart-beta
    title "joeynyc/skillscore 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a15ff4747fe5` · [字段定义](../../DATASET.md)*
