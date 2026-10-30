# SimpleAI2026/SimpleExcalidraw

⭐ 36 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/SimpleAI2026/SimpleExcalidraw) · [官网](https://excalidraw-phi-woad.vercel.app) · 个人维护 · 中文 README

**Excalidraw 中文 fork：加 AI 生成、多画布与绘图动画回放**

基于 Excalidraw 的定制 fork，面向需要中文手写体体验的画图用户：提供多画布切换、更多颜色选项、Mermaid 转换为 Excalidraw 元素、选中线段拖中点折弯等功能。AI 部分为画布内容生成：用户在面板填写 API 地址与模型，生成结果可替换/插入当前画布或新建画布，支持上传 md/txt/csv/pdf 灌入 Prompt（单文件 ≤2MB、Prompt 约 9000 字上限），密钥仅存 sessionStorage，生产建议走自有 BFF。动画回放模块将画布导出 SVG，用 WAAPI 按 stroke-dashoffset 回放笔迹。本地需 Node 与 Yarn Classic v1，也提供 Docker Compose。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 生成结果可替换/插入/新建画布，支持上传 md/txt/csv/pdf 灌入 Prompt
- 中文手写体（Zhushiti 回退栈）与多画布应用内切换
- Mermaid → Excalidraw 转换
- 绘图动画回放（SVG + WAAPI 笔迹回放，可暂停/取消/循环）

## 适用场景

- 用中文手写体绘制白板图并生成绘图过程动画
- 让 AI 根据文档或描述生成画布内容
- 把 Mermaid 图转换为可编辑的 Excalidraw 元素

## 场景标签

 · 领域:绘图/白板工具

## 证据(README 行号)

> L4: SimpleExcalidraw 是 Excalidraw 的定制 fork：中文手写体、多画布、AI 生成、Mermaid 转换、绘图动画回放。
> L15: - [x] AI 生成（替换 / 插入 / 新建画布；可取消；PDF/md/txt/csv 灌入 Prompt）
> L27: 1. 打开 AI 助手，填写 **API 地址**、**模型**；**密钥**在面板中粘贴（仅存当前标签页的 `sessionStorage`，关页即清）。

## 星数曲线

```mermaid
xychart-beta
    title "SimpleAI2026/SimpleExcalidraw 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-28 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f2002cd94a24` · [字段定义](../../DATASET.md)*
