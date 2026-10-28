# aigem/ComfyUI_KuAi_Power

⭐ 61 · Python · 推送 2026-05-28 · [GitHub](https://github.com/aigem/ComfyUI_KuAi_Power) · [官网](https://www.bilibili.com/video/BV1umCjBqEpt/) · 组织维护 · 中文 README

**ComfyUI 节点扩展：通过 API 调用 Sora2/Veo/Nano Banana 等模型**

ComfyUI 插件，通过 kuai.host API 服务接入 Sora2 与 Veo 视频生成、Nano Banana（Gemini）图像生成、AI 脚本生成等能力，提供文生视频、图生视频、多轮对话图像编辑、CSV 批量处理等节点，附图床上传、OCR 提取等工具节点。安装方式为克隆至 custom_nodes 目录并 pip 安装依赖，需配置 KUAI_API_KEY。全部节点提供中文界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Sora2/Veo 视频生成节点（文生/图生/任务查询/批量）
- Nano Banana Pro 多模态图像生成与多轮对话编辑
- AI 生成产品视频脚本/Sora 提示词
- CSV 批量处理与图床上传、OCR 工具节点

## 适用场景

- 在 ComfyUI 工作流中用提示词生成视频或图像
- 通过 CSV 批量生成/编辑图像或视频任务
- 为产品自动生成视频脚本与提示词

## 场景标签

`视频生成` `图像生成` `OCR` · 领域:内容生成

## 证据(README 行号)

> L3: ComfyUI 节点扩展，提供对 Sora2 和 Veo 视频生成模型、Nano Banana 图像生成以及 AI 脚本生成功能的支持。
> L18: 在节点参数中直接填写，或创建 `.env` 文件并设置环境变量 `KUAI_API_KEY=your_api_key_here`。
> L59: ### 🍌 Nano Banana 图像生成 (`KuAi/NanoBanana`)

## 星数曲线

```mermaid
xychart-beta
    title "aigem/ComfyUI_KuAi_Power 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 60 --> 63
    line [62, 61, 61]
```

2026-10-18 62 → 2026-10-28 61（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c0df2524db83` · [字段定义](../../DATASET.md)*
