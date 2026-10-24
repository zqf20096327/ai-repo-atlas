# xiaoranlingfeng/ppt-master-zit

⭐ 131 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/xiaoranlingfeng/ppt-master-zit) · 个人维护 · 中文 README

**ppt-master 的本机分支：AI 配图改走本地 ComfyUI 生成可编辑 PPTX**

基于官方 ppt-master v6.7.0（MIT, Hugo He）的个人定制分支，整套可编辑 PPTX 生成工作流与上游一致，差异是图片后端新增本地 comfyui 并默认启用：通过 ComfyUI HTTP API 运行 Qwen-Image-2.1 文生图工作流（默认），可选 MOSS-Image SFT 与 Z-Image Turbo，无需 API key、提示词不出本机。保留上游云端后端；新增逐页访谈门禁 D0–D9、导出后逐页校验门禁、图片清单断点续跑等。以 agent 技能目录形式安装，需自备 ComfyUI 与本地 GPU；Qwen/MOSS 权重为非商业许可，不可商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 ComfyUI 图片后端，COMFY_MODEL=qwen|moss|zit 三档可切
- Qwen-Image-2.1 默认工作流，原生 RGBA 透明图输出
- ComfyUI 未启动时后端自动拉起整合包并打开 Web UI
- 每 deck 一次的模型选择访谈门禁（D5）与导出后逐页校验

## 适用场景

- 在无 API key、要求提示词不出本机的环境下生成带 AI 配图的 PPT
- 用本地 GPU 按 deck 切换不同文生图模型做幻灯片配图
- 只想改一条提示词重渲染单张配图而不重跑整套 deck

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L11: **PPT Master + local ComfyUI image backend.** This is a personal-machine fork of ppt-master (v6.7.0, MIT, Copyright
> L26: - `templates/comfyui/qwen_image_2_1_t2i_api.json` — API-format export of the `image_qwen_image_2_1_t2i` workflow (Q


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e5792e9e5ab1` · [字段定义](../../DATASET.md)*
