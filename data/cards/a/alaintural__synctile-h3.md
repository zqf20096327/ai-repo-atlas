# alaintural/synctile-h3

⭐ 13 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/alaintural/synctile-h3) · [官网](https://pixedi.com/lab/minimax-h3-4k-synctile) · 个人维护

**在单卡 RTX 4090 上加速 MiniMax H3 生成并输出无接缝 4K 视频的脚本**

一个通过 ComfyUI HTTP API 驱动 MiniMax H3 视频模型的 Python 脚本（非 ComfyUI 节点）。fast 模式用 8-step 蒸馏 LoRA 加 int8 attention 后端，将 5.9 秒片段生成从 562 秒缩短到约 115 秒；4k 模式（SyncTile）先用 MiniMax H3 latent upscaler 放大，再以九个重叠 tile 每步在 latent 空间混合重采样，一次解码，输出 3840x2160 无接缝视频，约 11 分钟。需自备模型权重，24 GB VRAM 才能跑 4K，仅在 5 秒片段上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fast 模式：8-step LoRA + int8 attention，562s→约115s（4.9x）
- SyncTile：tile 间每步 latent 混合，无接缝 4K 输出
- 提供多组测量基准（含失败方案与 shimmer 指标）
- 逐 tile 处理，峰值显存等于单个 tile

## 适用场景

- 本地单卡生成更高分辨率 MiniMax H3 视频并放大到 4K
- 缩短 MiniMax H3 生成耗时
- 参考其基准数据选择加速方案

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L9: MiniMax H3 is an open-weights video model that also generates sound. On a 24 GB card it tops out around 1344 x 768, 
> L122: - This is a script that drives ComfyUI's HTTP API, not a ComfyUI node.

## 星数曲线

```mermaid
xychart-beta
    title "alaintural/synctile-h3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d9628d365a3c` · [字段定义](../../DATASET.md)*
