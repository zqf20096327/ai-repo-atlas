# Neon-Sparks/ComfyUI-NeonsStyleExplorer

⭐ 24 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/Neon-Sparks/ComfyUI-NeonsStyleExplorer) · 个人维护

**ComfyUI 风格提示词节点：3015 条风格目录与预览图库管理**

面向 ComfyUI 用户的风格提示词探索节点组：核心节点接收文本提示并拼接风格前缀（纯风格描述，不含画面内容指令），输出 natural/danbooru 格式文本，可附带 CLIP 编码；另含 LoRA 加载器与 checkpoint 加载器，各带按文件夹组织的预览图库。内置 3015 条风格条目（1419 条手写加 1596 条自 Krea 2 风格集导入），支持命名目录（每个图像模型一套预览）、随机摇选、逐条爬取生成预览、收藏与 JSON 导入导出。通过 ComfyUI Manager 或 git clone 安装，无额外依赖，Python 3.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3015 条风格条目，九大家族、三轴（style/format/finish）组织
- 命名目录：每个图像模型/项目独立的预览集、收藏与最近记录
- LoRA/Model Explorer 按文件夹自动归类并维护各自预览图库与触发词
- random_roll 随机摇选与 crawl 逐条爬取批量生成预览

## 适用场景

- 在 ComfyUI 里浏览和挑选图像生成风格提示词
- 为不同 checkpoint/LoRA 维护各自的生成效果预览图库
- 批量爬取风格批量出图，自动填充风格预览库

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: A style catalog node for ComfyUI. A style entry is a **style prefix** and nothing
> L10: * **Neons Style Explorer** — text in, text out
> L11: * **Neons Style Explorer (Encode)** — the same plus CLIP encode

## 星数曲线

```mermaid
xychart-beta
    title "Neon-Sparks/ComfyUI-NeonsStyleExplorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f272e8b45912` · [字段定义](../../DATASET.md)*
