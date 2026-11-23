# 47thtechcorner/RayCodes_FLUX3Klein

⭐ 3 · Python · 推送 2026-10-18 · [GitHub](https://github.com/47thtechcorner/RayCodes_FLUX3Klein) · [官网](https://youtu.be/lKaRGGc0LxA) · 个人维护

**用 2-3 句英文提示控制图像布局的 FLUX 3 Klein 生成管线**

基于 FLUX 3 Image Klein（Black Forest Labs，5.6B flow-map 架构）与 Diffusers 管线的图像生成控制器：将自然语言中的空间表述（如"在左侧""横跨顶部"）解析为归一化 0–1000 坐标网格，嵌入提示词以锁定主体与物体位置，无需训练或运行单独的 ControlNet。单个 checkpoint 同时处理文生图、角色一致性与局部编辑，输出 1024x1024 PNG 至 outputs/ 目录。以 Python 脚本提供，含三个内置测试场景，4GB VRAM 即可运行；Web UI 与 ComfyUI 集成列为未来计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言空间解析器自动生成 0–1000 坐标
- ControlNet-free 空间布局控制，单 5.6B checkpoint
- 内置三个测试场景管线（产品摆拍/赛博街景/建筑海报）
- README 声明 4GB VRAM 可运行

## 适用场景

- 电商产品图的固定版式摆拍生成
- 海报排版中指定文字横幅与主体的位置
- 多角色分镜图中分别放置人物位置

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L10: FLUX 3 Klein provides a unified 5.6B flow-map architecture that parses spatial bounding box coordinates embedded di
> L22: * **Unified Flow-Map Architecture**: Single 5.6B checkpoint handles text-to-image synthesis, character consistency,

## 星数曲线

```mermaid
xychart-beta
    title "47thtechcorner/RayCodes_FLUX3Klein 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-25 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ac9e74401a3b` · [字段定义](../../DATASET.md)*
