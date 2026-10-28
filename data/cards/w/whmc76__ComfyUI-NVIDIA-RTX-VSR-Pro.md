# whmc76/ComfyUI-NVIDIA-RTX-VSR-Pro

⭐ 45 · Python · Apache-2.0 · 推送 2026-08-10 · [GitHub](https://github.com/whmc76/ComfyUI-NVIDIA-RTX-VSR-Pro) · 个人维护

**ComfyUI 的 NVIDIA RTX 超分 Pro 节点：16K 输出与色彩保护**

作为 Comfy-Org/Nvidia_RTX_Nodes_ComfyUI 原节点的替代品（保留原节点 id，旧工作流可继续加载），通过 NVIDIA RTX VSR（nvidia-vfx）执行视频/图像超分辨率。将大尺寸目标经 15360px 中间结果再双三次插值到精确目标尺寸（最高 16384x16384），检测 RGB 通道塌缩并中止而非保存损坏图像，新增毫米+DPI 打印尺寸模式与保持宽高比开关。要求先移除原节点，需 Windows/Linux + NVIDIA RTX GPU，NVIDIA SDK 经 nvidia-vfx 包单独安装，仓库不含模型权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 保留原节点 id，替换后现有工作流继续加载
- 最高 16384x16384 精确输出，经 15360px RTX VSR 中间结果混合路径
- 检测红/绿/蓝通道塌缩并报错中止，防止静默保存损坏图像
- 新增 mm+DPI 打印尺寸模式与默认开启的保持宽高比开关

## 适用场景

- 在 ComfyUI 中将图像超分放大至 16K 用于打印
- 规避原版节点在 16384 边界出现蓝色通道丢失的问题
- 按物理打印尺寸（毫米+DPI）计算输出像素

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A workflow-compatible Pro replacement for
> L15: - Routes affected large targets through a verified `15360 px` RTX VSR
> L69: - Windows or Linux with an NVIDIA RTX GPU supported by `nvidia-vfx`

## 星数曲线

```mermaid
xychart-beta
    title "whmc76/ComfyUI-NVIDIA-RTX-VSR-Pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ace4027b4d13` · [字段定义](../../DATASET.md)*
