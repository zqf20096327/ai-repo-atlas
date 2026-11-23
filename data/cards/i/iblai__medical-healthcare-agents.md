# iblai/medical-healthcare-agents

⭐ 10 · MIT · 推送 2026-06-08 · [GitHub](https://github.com/iblai/medical-healthcare-agents) · [官网](https://ibl.ai/solutions/medical-healthcare) · 组织维护

**医疗健康场景的 13-agent OpenClaw/NemoClaw 配置包**

面向 ibl.ai 医疗健康方案段的 drop-in agent 配置：1 个 Care Assistant 父 agent 加 12 个专科子 agent（临床支持、患者教育、医学编码、合规培训、科研、保险预授权等），通过 sessions_spawn 委派任务，共享工作区传递产物，maxSpawnDepth=2 保持层级扁平。部署方式为将目录复制进 NemoClaw 沙箱的 .openclaw/ 路径，替换 Anthropic API key 与各第三方平台凭证后重算配置哈希并重载网关。附 10 个平台技能文件（Epic/Cerner FHIR、Availity、Micromedex、PubMed 等）。要求 PHI 处理遵循 HIPAA，临床 agent 均含免责声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1 父 + 12 子共 13 个医疗健康专科 agent，父 agent 经 sessions_spawn 委派
- 10 个第三方平台技能文件（Epic/Cerner FHIR、Availity、Micromedex、PubMed、UpToDate 等）
- 声明 PHI 处理遵循 HIPAA minimum necessary 标准，临床 agent 含免责声明
- 并发委派 maxConcurrent: 8 与 maxSpawnDepth: 2 的层级控制

## 适用场景

- 在 NemoClaw 沙箱中部署医疗健康 agent 套件
- 为医院 IT、编码、合规、患者教育等环节接入专科 agent
- 通过 FHIR/Availity/Micromedex 等平台技能让 agent 读取临床与保险数据

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Drop-in OpenClaw / NemoClaw agent configuration for the ibl.ai **Medical & Healthcare** solution segment — one Care 
> L14: The segment consists of **1 parent agent** and **12 specialist subagents** (13 agents total). All PHI handling foll
> L20: |`medical-healthcare-assistant`|Care Assistant|**PARENT** — entry point; interprets intent and delegates to special

## 星数曲线

```mermaid
xychart-beta
    title "iblai/medical-healthcare-agents 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `e2933eee78bb` · [字段定义](../../DATASET.md)*
