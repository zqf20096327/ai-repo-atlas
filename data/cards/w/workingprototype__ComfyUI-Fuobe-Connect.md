# workingprototype/ComfyUI-Fuobe-Connect

⭐ 3 · Python · MIT · 推送 2026-11-05 · [GitHub](https://github.com/workingprototype/ComfyUI-Fuobe-Connect) · [官网](https://fuobe.com) · 个人维护

**让 Fuobe 工作室使用本机 ComfyUI 的连接节点包**

一个 ComfyUI 自定义节点包，不含新增节点，作用是在浏览器端 Fuobe 创意工作室与本机 ComfyUI（默认 http://127.0.0.1:8188）之间建立受检连接。提供两种模式：直连模式由浏览器页面把任务发送到本机 ComfyUI；配对模式经 Fuobe 账号批准后，ComfyUI 通过 HTTPS 拉取任务，无需打开 Fuobe 页面，不开端口。每个工作流在进入 ComfyUI 前经 Python 检查：节点类型白名单、禁止磁盘/网络路径、文件加载器只能读 Fuobe 输入等；可配置信任工作室或设为 none，支持环境变量与无头机配对。

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

- 直连与配对两种模式，配对无需打开 Fuobe 页面且不开端口
- 每个工作流进入 ComfyUI 前经节点白名单与路径/文件访问规则检查
- 可通过设置界面、环境变量（FUOBE_CONNECT_ORIGINS 等）控制信任来源与行为
- 安装不引入 Python 依赖，复用 ComfyUI 自带的 aiohttp

## 适用场景

- 在浏览器里的 Fuobe 工作室中直接调用本机 ComfyUI 的 GPU
- 用 Safari、手机或无屏幕 PC 通过配对模式提交 ComfyUI 任务
- 为远程使用的 ComfyUI 限定哪些网站和节点可被访问

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: A ComfyUI custom node pack. It lets Fuobe, an open creative studio, use the ComfyUI on your own
> L62: - queue a workflow that passes Fuobe Connect's checks. Fuobe Connect checks every workflow here, in Python, before


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `ca5f5e1343a1` · [字段定义](../../DATASET.md)*
