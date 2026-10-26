# ProGamerGov/ComfyUI_pytorch360convert

⭐ 40 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/ProGamerGov/ComfyUI_pytorch360convert) · 个人维护

**ComfyUI 自定义节点集：360° 全景图像格式转换与处理**

将 pytorch360convert 库的函数封装为 ComfyUI 自定义节点，面向使用 ComfyUI 的图像生成用户，提供等距柱状全景图与立方体贴图、透视图之间的相互转换（E2C/C2E/E2P/E2E），以及 180°/360° 全景裁剪补齐、立体图拆分合并、接缝与极点遮罩生成、模型与 VAE 的圆形填充等辅助节点。依赖 pytorch360convert 库，可通过 ComfyUI-Manager、git clone、zip 解压或 ComfyUI registry 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 等距柱状/立方体贴图/透视图格式互转（E2C/C2E/E2P/E2E）
- 180°↔360° 裁剪补齐与立体/单目图像拆分合并
- 接缝遮罩与极点遮罩生成，配合局部重绘消除全景接缝
- 对模型与 VAE 的 Conv2d 层应用 x 轴圆形填充

## 适用场景

- 在 ComfyUI 工作流中转换 360° 全景图与立方体贴图格式
- 全景图生成后定位接缝并做局部重绘修复
- 将 180° 全景补齐为 360° 或拆分立体全景为单目图像

## 场景标签

`图像视频处理` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: This project implements the functions from pytorch360convert as custom ComfyUI nodes, along with a few additional us
> L69: The custom nodes added by this project are available under the 'pytorch360convert' heading in the node selection ta

## 星数曲线

```mermaid
xychart-beta
    title "ProGamerGov/ComfyUI_pytorch360convert 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4869322a0db5` · [字段定义](../../DATASET.md)*
