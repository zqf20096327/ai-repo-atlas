# Kuble-Lab/open-creative-director

⭐ 10 · JavaScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/Kuble-Lab/open-creative-director) · 组织维护

**本地优先的聊天式 AI 创意制作工具：规划并生成图像、视频、语音与动图**

面向需要在本地机器上完成创意内容生产的用户：用户用自然语言描述需求，经 OpenRouter 调用 LLM 作为 Director 进行规划与工具调用，按任务分发到 GPT Image 2（图像）、Seedance 2.5 等视频模型、ElevenLabs（语音）和 HTML/GSAP 动图渲染，结果内嵌聊天并本地存储。提供节点画布、角色一致性、品牌工作台、成本日志与 MCP 外部代理接入。必需 Node.js ≥22 与 OpenRouter key；ffmpeg、Poppler 及 Higgsfield/ElevenLabs/fal 账号为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天驱动制作：LLM 规划并通过工具调用执行生成
- 视频生成前展示模型卡片（价格、格式、推荐），点击才计费
- 节点视图可构建可复用生产流并发布为 Design App
- MCP 接口允许外部代理以个人密钥下单运行

## 适用场景

- 为品牌生成短视频广告与口播语音
- 跨集保持角色面部与声音一致的内容系列制作
- 在画布上编排批量图像/视频生产流程
- 对外提供受限额控制的 MCP 生成服务

## 场景标签

`视频生成` `图像生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: **Your personal AI creative director — a chat app that plans and produces images, videos, voice and motion graphics 
> L7: You describe what you want in plain language ("a 15-second vertical ad for my coffee brand, warm morning light"). Th
> L48: Requirements: Node.js ≥ 22, an OpenRouter API key. Optional: `ffmpeg` on your PATH (enables automatic visual consis

## 星数曲线

```mermaid
xychart-beta
    title "Kuble-Lab/open-creative-director 星数(近 2 点)"
    x-axis ["2026-10-31", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-31 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `bf115cd4295e` · [字段定义](../../DATASET.md)*
