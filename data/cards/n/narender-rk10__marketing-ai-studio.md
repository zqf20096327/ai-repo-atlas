# narender-rk10/marketing-ai-studio

⭐ 26 · TypeScript · 推送 2026-07-04 · [GitHub](https://github.com/narender-rk10/marketing-ai-studio) · 个人维护

**面向营销人员的多 Agent 营销内容生成平台（79 个专业 Agent）**

基于 Google ADK、FastAPI、React 18 构建的多 Agent 营销平台：通过 Gemini 3.1 Pro/Flash、Veo 3 等模型编排 79 个专业营销 Agent，分为品牌识别、视觉设计、社媒、视频、文案、广告、SEO、增长等类别，生成 Logo、社媒帖子、视频脚本、SEO 内容等资产。提供 XYFlow 交互画布、资产库、用量与分析追踪；生成物存储于 Google Cloud Storage。以统一 Docker 镜像部署，需配置 .env 环境变量；依赖 Google 生态（Gemini/Veo/Google Cloud），未见其他模型后端支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 79 个专业营销 Agent，按 10 个类别组织
- 多模型编排：Gemini 3.1 Pro/Flash、Nano、Veo 3 文生视频
- XYFlow 交互画布做可视化营销编排
- 统一 Docker 多阶段构建，单命令构建运行

## 适用场景

- 一站式生成品牌 Logo、社媒帖子和广告文案
- 用画布规划并编排整场营销活动
- 生成并管理视频脚本与 Veo 3 文生视频内容

## 场景标签

`多智能体` `AI 写作` `视频生成` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L242: MarketingAI Studio is a **form-driven, agent-orchestrated** marketing laboratory. Built with **Google ADK**, it le
> L253: |**3.1 Multi-Model Power**|Leveraging **Gemini 3.1 Pro**, **3.1 Flash**, **Gemini Nano**, **Gemini Banana**, and *

## 星数曲线

```mermaid
xychart-beta
    title "narender-rk10/marketing-ai-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `70164b710297` · [字段定义](../../DATASET.md)*
