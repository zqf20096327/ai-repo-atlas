# kaili-yang/ComfyUI-Workflow-Debugger

⭐ 21 · Python · 推送 2026-08-06 · [GitHub](https://github.com/kaili-yang/ComfyUI-Workflow-Debugger) · [官网](https://comfy-workflow-debugger.netlify.app/) · 个人维护 · 中文 README

**浏览器端离线静态分析工具：诊断并修复 ComfyUI 工作流 JSON**

免费、离线优先的浏览器工具，面向 ComfyUI 用户：上传工作流 JSON（标准图格式或 API 格式），在本地浏览器内做静态分析，按严重度列出断线连接、类型不匹配、孤立节点、循环依赖、无效参数等诊断，并提供一键自动修复（重接断线、插入类型转换节点、恢复文件引用等），修复后可下载 JSON 重新导入 ComfyUI。可选连接运行中的 ComfyUI 实例以检查缺失自定义节点。无需本地安装 ComfyUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持标准图格式与 API 格式工作流 JSON 的本地静态分析
- 按严重度（错误/警告/提示）分组的诊断清单
- 一键自动修复：重接断线、插入类型转换节点、重置无效参数等
- 可选连接运行中的 ComfyUI 实例检查缺失自定义节点

## 适用场景

- 工作流加载失败或节点报错时快速定位问题
- 自动修复类型不匹配与断线连接后重新导回 ComfyUI
- 排查大型工作流中的失效节点与无效参数

## 场景标签

 · 领域:AI 图像生成/ComfyUI 工具链

## 证据(README 行号)

> L17: **ComfyUI Workflow Debugger** is a free, offline-first browser tool built to solve your **broken ComfyUI workflows,
> L88: To debug a broken ComfyUI workflow, export your workflow as a `.json` file (either standard or API format) and drag

## 星数曲线

```mermaid
xychart-beta
    title "kaili-yang/ComfyUI-Workflow-Debugger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6fd9ab7647fa` · [字段定义](../../DATASET.md)*
