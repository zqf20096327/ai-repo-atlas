# siamcafe/bomllm

⭐ 42 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/siamcafe/bomllm) · 个人维护

**Apple Silicon 自托管 AI 平台：Mac Mini 跑推理/泰语优化**

以 Mac Mini M4 Pro 48GB 为核心的自托管多模态 AI 生产栈：通过 MLX 运行 Fable 732（27B nvfp4，约 21 tok/s，MTP 推测加速 2-3 倍）与本地编码模型 MiMo-V2.6 Q4（37 tok/s），云端 GLM-5.3 处理生产编码；另由 i9 + 2× RTX 5060 Ti 运行 ComfyUI/FLUX 图像生成、SiangTTS 泰语语音与 YuE2/ACE-Step 音乐生成。网络经 Tailscale 组网、Cloudflare Tunnel 提供 HTTPS，通过 git clone 加 bootstrap 脚本部署。README 面向泰语场景，含成本对比与编码基准表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Fable 732（Qwen3.8-27B base，nvfp4 MLX）约 21 tok/s，MTP 推测 2-3×
- 本地 MiMo-V2.6 Q4 37 tok/s 草稿 + 云端 GLM-5.3 复审的编码分工流程
- 图像/泰语语音/音乐生成（ComfyUI+FLUX、SiangTTS、YuE2+ACE-Step）
- 5 个生产通道 + LINE 机器人，含直播弹幕视觉分析与图表实时解说

## 适用场景

- 用一台 Mac Mini 自托管替代云 LLM API 日常用量
- 搭建泰语优化的多模态内容生产管线（文本/图像/语音/音乐）
- 直播场景做实时弹幕问答与图表 AI 解说

## 场景标签

`推理引擎` `图像生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L8: It now does **inference, coding, image generation, voice synthesis, music, and live streaming** — all self-hosted.
> L10: One **Mac Mini M4 Pro 48GB** runs Fable 732 (27B nvfp4 MLX) at **~21 tok/s** with MTP 2-3× speculation.

## 星数曲线

```mermaid
xychart-beta
    title "siamcafe/bomllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0438bbd83896` · [字段定义](../../DATASET.md)*
