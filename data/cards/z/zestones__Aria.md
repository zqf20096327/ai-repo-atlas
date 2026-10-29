# zestones/Aria

⭐ 61 · TypeScript · 推送 2026-05-18 · [GitHub](https://github.com/zestones/Aria) · [官网](https://aria.vgtray.fr) · 组织维护

**工厂预测性维护 AI 应用：知识库+五 Agent 检测诊断设备故障**

面向工业设备维护的多 Agent 应用：KB Builder 用 Claude Opus 视觉读取厂商 PDF 手册并通过问卷捕获老师傅经验构建知识库；Sentinel 监控实时信号并预测漂移；Investigator 用 Opus 4.7 扩展思考在沙箱容器中运行 Python 计算退化速率做根因诊断；随后生成工单，并提供自然语言 Q&A。数据存于 TimescaleDB，Agent 经 17 个 MCP 工具访问数据。内置模拟器两种模式供演示，Docker Compose 一键启动，需 ANTHROPIC_API_KEY。为黑客松获奖项目（Anthropic x Cerebral Valley）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个 Agent 流水线：检测→诊断→工单→记忆
- PDF 手册视觉抽取 + 操作员问卷构建维护知识库
- Investigator 在沙箱容器运行 Python 计算退化速率
- Docker Compose 一键启动全栈并内置设备模拟器

## 适用场景

- 工厂在设备故障前获得预警与根因诊断
- 把老师傅经验与厂商手册沉淀为可持续维护的知识库
- 自动生成含备件清单与干预时间窗的工单

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L20: **ARIA is the bridge.** Drop in the manufacturer's PDF, answer some questions, and you're live in ten minutes. Afte
> L32: - **Sentinel** — watches live signals against the KB; detects breaches, runs forecast on signal tails, and judges w
> L92: **Agents.** Anthropic Python SDK against Claude Opus 4.7 (reasoning + PDF vision) and Sonnet (routine tool work). T

## 星数曲线

```mermaid
xychart-beta
    title "zestones/Aria 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-29 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `13e39747bdaf` · [字段定义](../../DATASET.md)*
