# UNfukashigi/Anima-LoRA-Factory

⭐ 84 · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/UNfukashigi/Anima-LoRA-Factory) · 个人维护 · 中文 README

**无需编程知识、训练 Anima 扩散模型 LoRA 的 GUI 工具**

面向 Anima 图像生成模型的 LoRA 训练 GUI 工具，目标用户为不具备编程知识的创作者。运行 start.bat 即自动安装训练引擎 sd-scripts 并按硬件配置合适的 PyTorch；内置 WD14 Tagger 自动打标与可视化标签编辑器、实时进度显示、最近 30 次训练历史记录、训练完成自动转换为 ComfyUI 可用格式，并可训练结束后自动关机。原生支持 NVIDIA RTX 50（Blackwell/sm_120），自动检测 CUDA 问题并配置 CUDA 13.0 等环境。要求 Windows 10/11 64bit、NVIDIA GPU、Python 3.10，需自行下载 Anima Base Model、Qwen3 Text Encoder 与 Qwen Image VAE；派生模型训练不在官方支持范围。以 zip 安装包分发，另有 SDXL 版本仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- start.bat 一键自动搭建 sd-scripts 训练环境与硬件适配的 PyTorch
- 内置 WD14 Tagger 自动打标与可视化标签编辑器
- 原生支持 RTX 50（Blackwell/sm_120），自动配置 CUDA 13.0
- 训练完成自动输出 ComfyUI 可直接使用的 LoRA 格式

## 适用场景

- 不写代码就能训练 Anima 模型的 LoRA
- 边看图片边编辑数据集的标签和触发词
- 在 RTX 50 系列新显卡上进行 LoRA 训练并规避 CUDA 报错
- 训练好的 LoRA 直接放进 ComfyUI 使用

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: Anima LoRA Factory は、次世代画像生成モデル Anima の LoRA 学習を、プログラミングの知識なしで誰でも簡単に行えるように設計された GUI ツールです。 特に最新の NVIDIA RTX 50シリーズ (
> L21: start.bat を実行するだけで、必要な学習エンジン (sd-scripts) やハードウェアに最適な PyTorch を自動的にセットアップします。
> L51: 学習完了後、自動的に ComfyUI で即座に使用可能な形式へ変換・出力します。

## 星数曲线

```mermaid
xychart-beta
    title "UNfukashigi/Anima-LoRA-Factory 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25", "2026-10-30"]
    y-axis "stars" 79 --> 85
    line [80, 82, 84, 84]
```

2026-10-18 80 → 2026-10-30 84（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8241ebd855d3` · [字段定义](../../DATASET.md)*
