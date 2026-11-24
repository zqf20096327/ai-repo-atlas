# langchain-ai/design-agent

⭐ 670 · JavaScript · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/langchain-ai/design-agent) · 组织维护

**团队可部署的品牌设计 agent：对话产出图像/幻灯片/视频**

LangChain 开源的 Content Studio 设计 agent，基于 Deep Agents 构建，通过 Slack 对话接收需求并返回符合品牌的成品文件（图片、幻灯片、图表、动画视频）。机制上：每个线程一个 LangSmith Linux 沙箱（含 Chrome、FFmpeg、HyperFrames、D2），35 个技能按需加载路由工作流，品牌以 token 形式作为代码约束渲染，每次渲染做代码化检查，支持异步子代理与团队/个人双层记忆。部署需 LangSmith 账户（Managed Deep Agents 公测）与模型密钥；本地 demo 需 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35 个技能按需加载，router skill 选择工作流
- 品牌以代码化 token 约束，渲染时自动检查颜色/字体/对比度
- 异步子代理并行分工，团队与个人双层记忆
- 本地 demo 以 scripted model 运行，无需 API key

## 适用场景

- 在 Slack 里让 agent 生成各平台尺寸的品牌宣传图
- 从 CSV 生成周报图表与演示文稿
- 让 agent 制作带配音配乐的产品发布短片
- 为网络研讨会片段生成字幕

## 场景标签

`图像生成` `视频生成` `AI 助手` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L17: **Content Studio is the design agent LangChain runs, now open source.** Add your brand and deploy it
> L35: Content Studio is a Deep Agents agent deployed on
> L39: delivers.

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/design-agent 星数(近 23 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 0 --> 736
    line [3, 6, 42, 266, 459, 508, 528, 542, 597, 606, 610, 611, 615, 616, 619, 628, 631, 633, 640, 661, 665, 670, 670]
```

2026-10-26 3 → 2026-11-24 670（+667）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `96462b099567` · [字段定义](../../DATASET.md)*
