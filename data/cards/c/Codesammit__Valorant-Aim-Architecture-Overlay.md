# Codesammit/Valorant-Aim-Architecture-Overlay

⭐ 54 · HTML · 推送 2026-10-27 · [GitHub](https://github.com/Codesammit/Valorant-Aim-Architecture-Overlay) · 个人维护

**Valorant 屏幕分析叠加层：AI 注意力热图与 DNS 路由优化**

面向 Valorant 玩家的桌面叠加层工具，通过屏幕捕获读取游戏画面（自称不读写游戏内存、不注入进程），调用 Claude API 与 OpenAI Vision API 生成注意力热图、准星分布分析与回合总结，并通过 Discord 机器人发送赛后数据。另含 DNS 提供商切换（Cloudflare/Google/AWS Route53）与基于 Kubernetes 本地微集群、RocketMQ 的部署架构。README 声明仅供教育与分析用途，运行风险自担；下载链接处仅有 'Download' 占位文本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude API 与 OpenAI Vision API 处理屏幕截图，生成注意力热图与回合叙事
- 准星位置预测（基于专业选手移动数据训练的线性层）
- DNS 提供商自动切换（Cloudflare/Google/AWS/OpenDNS）
- Discord 机器人发送赛后分析，支持多语言输出

## 适用场景

- 赛后查看自己的准星与注意力分布数据
- 通过 Discord 接收多语言比赛总结
- 切换 DNS 提供商以观察对局延迟差异

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L35: - **Claude API** processes screen captures to identify teammate positions without accessing game memory
> L36: - **OpenAI API** generates natural-language summaries of round outcomes based on visual patterns

## 星数曲线

```mermaid
xychart-beta
    title "Codesammit/Valorant-Aim-Architecture-Overlay 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-28 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `e898c2503844` · [字段定义](../../DATASET.md)*
