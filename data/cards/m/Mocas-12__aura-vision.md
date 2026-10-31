# Mocas-12/aura-vision

⭐ 31 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Mocas-12/aura-vision) · [官网](https://aura-vision-beige.vercel.app) · 个人维护 · 中文 README

**手机摄像头实时 AI 物体识别网页应用，赛博朋克 UI**

基于 React 19 + TypeScript + Vite 的手机端视觉识别应用：摄像头取景，自动每 5 秒（或手动按钮）对画面中心物体进行识别，图像裁剪压缩后经 Cloudflare Worker 转发至 NVIDIA 多模态视觉模型（llama-3.2-11b-vision），结果以中文名字+介绍形式经 SSE 流式呈现，后端不可流式时降级为打字机动画。含免费配额（每设备 15 次）与激活码永久解锁机制，API key 仅存于服务端。面向普通用户，部署至 GitHub Pages。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动/手动双识别模式，SSE 流式输出降低首 token 延迟
- NVIDIA llama-3.2-11b-vision 模型，失败自动回退至 90B 版本
- 每设备 15 次免费配额与激活码解锁机制
- API key 仅存服务端（Worker/Vercel），前端无密钥

## 适用场景

- 用手机摄像头即时识别身边物体并获取中文介绍
- 阅读多语言包装文字时获取中文说明
- 作为可部署的 Cloudflare Worker + 视觉 LLM 应用模板学习

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L25: - 🎯 **Smart Recognition**: Powered by the NVIDIA multimodal vision model (llama‑3.2‑11b‑vision‑instruct), outputs a
> L50:     C --> D[🧠 NVIDIA multimodal model<br/>llama-3.2-11b-vision]
> L57: 3. **Model inference**: The Worker calls the NVIDIA Integrate API (`/v1/chat/completions`) and gets the multimodal 

## 星数曲线

```mermaid
xychart-beta
    title "Mocas-12/aura-vision 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-31 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8811ebb82d43` · [字段定义](../../DATASET.md)*
