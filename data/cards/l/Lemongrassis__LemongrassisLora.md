# Lemongrassis/LemongrassisLora

⭐ 3 · Python · GPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/Lemongrassis/LemongrassisLora) · 个人维护

**本地 Web 工作室：一站式训练 LoRA/LoKr/LoHa 适配器**

本地网页工作室，用于训练 LoRA/LoKr/LoHa 适配器，支持 Anima、Krea 2 和 MOSS Image 三个基础模型家族。流程覆盖数据集导入与整理、预处理、打标编辑、正则集构建、训练队列、监控到测试生成，全部在浏览器内完成。通过 block swap、fp8/INT8、缓存和 NaViT packing 降低显存占用，最低 6 GB 显存可训练 Anima；支持 Tailscale/ngrok/Cloudflare 远程访问与手机端操作，也可在 Colab 运行。仅支持 NVIDIA GPU，不支持 AMD 与 Apple Silicon。代码 GPL-3.0 许可，fork 自 AnimaLoraStudio。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据集→整理→打标→训练→生成全流程在同一浏览器窗口
- 支持 LoRA/LoKr/LoHa/DoRA 等多种适配器算法与多种优化器
- block swap、fp8/INT8、缓存等显存优化，最低 6 GB 显存起训
- Tailscale Funnel/ngrok/Cloudflare 远程访问，手机适配界面

## 适用场景

- 在自己的 NVIDIA GPU 上为 Anima/Krea 2/MOSS 训练 LoRA 并直接加载到 ComfyUI
- 从 Booru 抓取图片建数据集并批量编辑标签
- 通过手机或远程链接监控训练进度与样图

## 场景标签

`微调` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: **A local web studio for training LoRA / LoKr adapters for Anima, Krea 2 and MOSS Image.**
> L21: Dataset → curation → preprocess → tags → reg set → training → queue → generation. The sidebar shows where you are, 
> L170: |**GPU**|NVIDIA 6 GB (Anima) / 12 GB (Krea 2, MOSS)|NVIDIA 16 GB+|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `fddde034a284` · [字段定义](../../DATASET.md)*
