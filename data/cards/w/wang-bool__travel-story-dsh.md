# wang-bool/travel-story-dsh

⭐ 8 · JavaScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/wang-bool/travel-story-dsh) · 个人维护 · 中文 README

**DSH 插件：AI 规划行程、查天气并驱动地图**

将 Travel Story 旅行应用（前端 + 后端 + 数据）作为插件运行在 DeepSeek Harness 中的插件：Host 端注册 18 个 DSH 工具（搜索地点、查天气预报、创建/编辑行程、计算路线、控制地图视图），并内置 travel-story-planner skill 指导模型按固定流程规划行程；面板打开时自动注入当前行程上下文，agent 搜索与修改过程在活动流中可见。经 dsh plugin add 一条命令安装，零运行时依赖；地点搜索与路线需可选配置高德/LocationIQ key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Host 端注册 18 个工具：搜索地点、查天气、编辑行程、计算路线并驱动地图
- 内置 travel-story-planner skill，按「需求沟通→天气→攻略→时间账→录入」流程规划
- 面板打开时自动注入当前行程/站点上下文到对话
- 零部署：dsh plugin add 一条命令安装，Host 端纯 Node ESM

## 适用场景

- 让 AI 根据天气和攻略规划逐日行程并录入地图
- 在对话中引用「这一站」「第 5 天」直接修改行程
- 逐日查看地图路线播放与天气展示

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: 把 Travel Story 完整搬进 DeepSeek Harness（DSH）的插件版本——**不是 iframe 套壳，而是整个应用（前端 + 后端 + 数据）自包含地跑在 DSH 里**。
> L32: - **模型直接帮你规划行程**：Host 端注册 18 个 DSH 工具（`list_trips` / `get_trip` / `search_places` / `get_weather` / `create_trip` /

## 星数曲线

```mermaid
xychart-beta
    title "wang-bool/travel-story-dsh 星数(近 3 点)"
    x-axis ["2026-11-12", "2026-11-13", "2026-11-26"]
    y-axis "stars" 6 --> 9
    line [7, 8, 8]
```

2026-11-12 7 → 2026-11-26 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `36ebe1315528` · [字段定义](../../DATASET.md)*
