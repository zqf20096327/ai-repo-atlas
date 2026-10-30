# Icyoung/ComfyUI-MiniMaxH3-TeaCache

⭐ 20 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/Icyoung/ComfyUI-MiniMaxH3-TeaCache) · 个人维护 · 中文 README

**ComfyUI 插件：用 TeaCache 时间步缓存加速 MiniMax H3 视频生成**

面向 ComfyUI 用户的 MiniMax H3 视频生成加速节点：实现 TeaCache（Liu et al. 2024）的自适应时间步缓存，当相邻步输入增量低于阈值时复用上一步的 DiT 前向输出，减少 20 次前向中的重复计算。作者实测 fl2va int8_convrot 场景从 306.22s 降至 102.08s（-66.7%，3.0×），并声明缓存决策确定性、同种子下结果位级一致。纯 Python 实现，Linux/Windows/macOS 可用，通过官方 set_model_unet_function_wrapper 接入，不修改 ComfyUI 核心。对比项：闭源的 TE-Speed-MiniMaxH3。多项任务（多 prompt 扫描、多项式校准、质量门）仍在待办清单中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- TeaCache 时间步缓存：输入增量低于阈值时复用前向输出
- 作者实测 306.22s→102.08s（3.0×加速，NVIDIA CMP 170HX）
- 纯 Python、无编译、不修改 ComfyUI 核心的节点接入
- 缓存决策确定性：同种子+同 prompt 输出位级一致

## 适用场景

- 我在 ComfyUI 里跑 MiniMax H3 视频生成，想缩短采样时间
- 我在 Linux/macOS 上需要一个开源的 H3 加速方案（闭源版仅 Windows .pyd）
- 我想通过 rel_l1_thresh 阈值权衡加速与画质

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: Timestep-caching acceleration for **MiniMax H3** video generation in ComfyUI. Open-source Linux/Windows/macOS. Writt
> L42: |model.py patch|Ships a modified `comfy/ldm/minimax/model.py`|Uses ComfyUI's official `set_model_unet_function_wrap
> L62: UNETLoader → MiniMaxH3 TeaCache → CFGGuider / BasicGuider → SamplerCustomAdvanced

## 星数曲线

```mermaid
xychart-beta
    title "Icyoung/ComfyUI-MiniMaxH3-TeaCache 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d3ff66b004fb` · [字段定义](../../DATASET.md)*
