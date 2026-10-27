# William-Lu-stack/Flawless

⭐ 768 · Python · NOASSERTION · 推送 2026-08-14 · [GitHub](https://github.com/William-Lu-stack/Flawless) · 个人维护 · 中文 README

**面向 Kubernetes 与云基础设施的 AI SRE 闭环运维平台**

CISRE 把基础设施的风险发现、证据采集、根因诊断、人工审批、受控变更、同目标回读、恢复验证与经验沉淀连接成可审计闭环，供 SRE 与平台/领域运维团队使用。架构上模型负责理解规划，Skill 承载处置知识，插件提供可组合能力，Harness 负责状态权限编排；Kubernetes 已完整闭环，数据库/VM/存储/网络等领域以插件合同方式接入。所有真实变更必须经过类型化动作、策略与爆炸半径、人工审批与恢复验证，模型输出不能直接成为执行指令。本地以 Python venv + requirements.txt 启动后端、npm 构建前端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发现→取证→诊断→审批→执行→回读→恢复验证的可审计闭环
- Plugin-first 架构：领域能力以插件与 Skill 交付，核心零改动
- 真实变更必须经人工审批与同目标回读，插件无法绕过门禁
- 核心通过 cisre.kernel.ports/v1 四个可替换端口支撑规模化

## 适用场景

- Kubernetes 故障的自动取证、诊断与受控恢复
- 定时/手动 AI 巡检发现基础设施风险
- 数据库、VM、存储等团队以插件方式接入统一运维闭环

## 场景标签

 · 领域:云原生运维/AIOps

## 证据(README 行号)

> L3: CISRE（Cloud Infrastructure Site Reliability Engine）把基础设施的风险发现、证据采集、根因诊断、人工审批、受控变更、恢复验证和经验沉淀连接成一条可审计闭环。
> L9: 模型负责理解、规划和解释；Skill 负责领域处置知识；插件负责提供可组合能力；Harness 负责状态、权限和编排；受控执行器负责真实变更；Verifier 负责证明目标已经恢复。
> L17: 执行 API 返回成功、模型声称成功或旧实例仍然健康，都不等于故障恢复。只有真实目标的新证据满足恢复合同，任务才会闭环。

## 星数曲线

```mermaid
xychart-beta
    title "William-Lu-stack/Flawless 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 766 --> 772
    line [771, 767, 768]
```

2026-10-18 771 → 2026-10-27 768（-3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `9216c7aa6a88` · [字段定义](../../DATASET.md)*
