# maciejtajber/ComfyUI-StudioLight

⭐ — · [GitHub]() · 个人维护

**ComfyUI 3D 摄影棚布光与一致性重打光节点**

面向 ComfyUI 的自定义节点，用户在 3D 相机空间中摆放 Key/Fill/Rim 三盏灯（球坐标方位角/仰角/距离）、选择摄影级光效附件、按开尔文控制色温，对既有照片、成品渲染或生成草稿进行重打光。引擎先从源图估算法线、深度与本征反照率并复用，再经阴影 raymarching 输出直接重打光预览，可选 FLUX.1 模型做二次细化；支持叠加环境光或替换主体光两种合成契约。以 git clone 安装，附带 Create 与 Relight 两个工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3D C-Stand 坐标（方位角/仰角/距离）与三区瞄准指针控制三盏独立灯
- 黑体开尔文 2000K–10000K 色温控制与摄影光效附件孔径建模
- 阴影 raymarching 与 18% 灰球/镜面铬球实时探针、俯视雷达
- Add Studio Light 与 Replace Subject Light 两种合成契约

## 适用场景

- 对同一张人像做多种布光方案而不改变人物与场景
- 从照片重建反照率后替换主体光照
- 在 ComfyUI 生成流程中用空间布光替代纯提示词描述光照

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L8:  ComfyUI Custom Node
> L26: Stop prompt gambling. StudioLight brings real, three-dimensional studio lighting control directly into ComfyUI.
> L28: Instead of typing descriptive text and hoping the diffusion model understands your intent, you position physical li

## 星数曲线

```mermaid
xychart-beta
    title "maciejtajber/ComfyUI-StudioLight 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 4 --> 7
    line [5, 6]
```

2026-11-08 5 → 2026-11-21 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `8c38ba4b19e4` · [字段定义](../../DATASET.md)*
