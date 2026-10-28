# autodesk-platform-services/aps-viewer-ai-render

⭐ 20 · JavaScript · MIT · 推送 2026-03-27 · [GitHub](https://github.com/autodesk-platform-services/aps-viewer-ai-render) · [官网](https://aps-viewer-ai-render.autodesk.io) · 组织维护

**基于 APS Viewer 场景与 Stable Diffusion 生成照片级渲染图的示例应用**

Autodesk 平台服务团队的示例项目：用户在 Web 应用中从 ACC hub 选择设计，用 APS Viewer 渲染并配置场景，通过截屏生成输入图像，经 Comfy.icu 调用 Stable Diffusion 工作流（ControlNet），结合正/负文本提示词生成照片级图像，并与原图对比展示。运行需 Node.js（LTS）、APS 账号与应用、Comfy.icu 账号，配置 .env 后 npm start 启动。MIT 许可，提供在线只读演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Viewer 截屏作为输入图像，经 Comfy.icu API 触发 Stable Diffusion 工作流
- 支持正/负文本提示词组合生成输出图像
- 输入与输出图像并排对比展示

## 适用场景

- 设计师从设计场景快速生成照片级渲染图
- 学习 APS Viewer 与生成式 AI 的集成方式
- 参考 Comfy 工作流通过 HTTP API 调用的实现

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Rendering is a required and sometimes painful part of the process in the lives of designers. With a quick search usi
> L23: To make this possible, we take advantage of Stable Diffusion.

## 星数曲线

```mermaid
xychart-beta
    title "autodesk-platform-services/aps-viewer-ai-render 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c2a20de01cb1` · [字段定义](../../DATASET.md)*
