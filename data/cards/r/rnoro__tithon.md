# rnoro/tithon

⭐ 14 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/rnoro/tithon) · [官网](https://rnoro.github.io/tithon/) · 个人维护

**让 Jupyter 内核与输出在客户端断开后存活的守护进程工具**

由主机上长驻 daemon 接管 ipykernel 会话：内核以 setsid 脱离运行，全部 iopub/shell 消息逐字写入 SQLite/WAL 日志并折叠为快照，图片等富输出按哈希存为文件，客户端重连后凭序号续流，无需重启。配套 VS Code 扩展提供 .pynb 笔记本编辑器（磁盘格式为纯 percent .py），CLI 支持提交代码、附加事件流与 .ipynb 导入导出。面向远程 GPU 主机上跑长任务的开发者。要求 Python 3.11+ 与 Unix-like 主机（Windows 需 WSL），自述处于 alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内核 detached 运行，daemon 崩溃/重启后内核存活并可重连续流
- 消息逐字 journal 到 SQLite/WAL，重连获得快照+无缝增量流
- 富输出按哈希存为真实文件而非 base64 内嵌，ipywidgets 状态镜像可恢复
- VS Code 扩展的 .pynb 格式为纯 percent .py，输出与源码分离

## 适用场景

- SSH 到远程 GPU 机跑长任务，关掉编辑器后回来继续查看实时输出
- 同一会话从第二客户端打开并恢复流式输出
- 让 AI agent 以纯 .py 和真实图片文件形式消费 notebook 源码与输出

## 场景标签

 · 领域:开发工具/交互式计算

## 证据(README 行号)

> L36: > And in the era of AI agents, one more: a `.ipynb` is JSON bloat — the same
> L40: > model burns thousands of tokens on and still can't read. **Don't feed your AI

## 星数曲线

```mermaid
xychart-beta
    title "rnoro/tithon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c40af70c844d` · [字段定义](../../DATASET.md)*
