# selftune-dev/selftune

⭐ 18 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/selftune-dev/selftune) · [官网](https://selftune.dev) · 组织维护

**AI agent 技能的观测与自动改进工具包**

面向使用 Claude Code、Codex、OpenCode 等 agent 工具的开发者：通过实时 hooks 捕获真实会话中的查询与技能调用，检测技能描述与用户实际表达之间的失配（如沉默失败），生成多个改写提案并在真实评估集上验证后自动改写技能描述，部署前自动备份。以 npm 包分发（含 CLI 与 SKILL.md），另有本地 SQLite 存储、React 仪表盘桌面端、可选自托管 Docker 镜像与托管云。本地优先，原始转录默认不上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七个实时 hooks 捕获查询、技能调用与纠正信号
- 从真实会话学习用户表达并自动改写技能描述，部署前经评估集验证与备份
- 提供 verify/eval/search-run/improve 等技能测试与改进命令
- 桌面端、CLI、自托管与托管云共用同一本地 SQLite 数据

## 适用场景

- 技能装多了但经常不被触发，想看健康度并自动改进路由
- 发布技能前测试路由、发布后收集贡献者信号迭代
- 非编码场景（幻灯片、研究流程）中修复'说了没反应'的技能失配

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L20: selftune is an open-source agent skill observability toolkit that watches how your AI agent uses its skills, detect
> L24: Works with **Claude Code** (primary), **Codex**, **OpenCode**, **Cline**, **OpenClaw**, and **Pi**. Bun-native with

## 星数曲线

```mermaid
xychart-beta
    title "selftune-dev/selftune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `859be77d29f0` · [字段定义](../../DATASET.md)*
