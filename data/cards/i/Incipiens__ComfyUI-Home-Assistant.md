# Incipiens/ComfyUI-Home-Assistant

⭐ 15 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Incipiens/ComfyUI-Home-Assistant) · 个人维护

**在 Home Assistant 中调用 ComfyUI 生成图像的非官方集成**

Home Assistant 自定义组件，通过 HA 的 AI Task 平台 Generate Image 动作向 ComfyUI API 发起请求生成图像。配置时填入 ComfyUI 服务器 URL、超时与导出的工作流 JSON 路径，节点 ID 可自动检测；0.5.0 版本加入 WebSocket API 进度跟踪与重新配置支持。提示词可插入 HA 传感器状态（如天气、时间）实现动态生成。限制：目前仅支持文生图，不支持图生图附件。可经 HACS 安装或手动上传文件。

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

- 基于 Home Assistant AI Task 平台的 Generate Image 动作
- 0.5.0 加入 ComfyUI WebSocket API 进度跟踪与节点自动检测
- 提示词模板可引用 HA 传感器状态动态生成图像
- 支持 HACS 安装与手动安装两种方式

## 适用场景

- 在家庭自动化场景中按传感器状态生成图像（如天气画面）
- 通过 HA 的动作调用 ComfyUI 工作流生成图片

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: This is an unofficial custom component for Home Assistant that allows for the integration of ComfyUI into Home Assis
> L41: Once you add it, you can test it by going to Developer Tools, Actions, and select "Generate Image." The entity shou

## 星数曲线

```mermaid
xychart-beta
    title "Incipiens/ComfyUI-Home-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0002dd37eec5` · [字段定义](../../DATASET.md)*
