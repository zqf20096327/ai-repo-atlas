# z1xz277/nexa

⭐ 3 · TypeScript · 推送 2026-11-26 · [GitHub](https://github.com/z1xz277/nexa) · [官网](https://info.nexa-web.workers.dev/) · 个人维护

**Windows 11 编码工作区：集成代理与逐次权限控制**

面向 Windows 11 的桌面编码工作区，整合项目文件、Monaco 代码编辑器、xterm 终端与可调用工具的 agent，每次运行前通过 Ask/Agent/Full Access 三种模式显式授权文件访问与命令执行；Full Access 需宿主签发短时效单次授权。基于 Electron，agent 核心通过 IPC 运行，提供 NVIDIA NIM 与 OpenRouter 适配器及模型发现、流式输出与回退。需 Node 20+，提供浏览器预览模式与 Windows 安装包构建流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ask/Agent/Full Access 三档逐次权限控制，宿主签发短时效单次授权
- 文件操作在非法路径、符号链接逃逸等场景下默认失败关闭
- NVIDIA NIM 与 OpenRouter 适配器，支持模型发现与回退
- 更新包 SHA-512 校验并支持 Authenticode 签名

## 适用场景

- 在 Windows 11 上获得集编辑器、终端与 agent 的编码环境
- 需要细粒度控制 agent 文件写入与命令执行权限
- 本地管理多模型接入并统一维护 API 密钥

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Nexa is a focused Windows 11 desktop workspace for coding. It combines project files, a code editor, a terminal, and
> L48: |Agent|Read and change files inside the project|Writes, edits, memory updates, and commands require approval|
> L59: - `src/core/agent.ts`: streaming loop, tool dispatch, approvals, and run lifecycle.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6a5ab853b814` · [字段定义](../../DATASET.md)*
