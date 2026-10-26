# andybbruno/deepagents-docker

⭐ 32 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/andybbruno/deepagents-docker) · 个人维护

**为 Deep Agents 提供 Docker 沙箱后端的 Python 库**

deepagents-docker 是一个 Python 库，为 LangChain 的 Deep Agents 提供 DockerSandbox 后端：创建对象即启动长驻 Docker 容器，agent 执行的所有 shell 命令（库安装、cURL 下载、文件改动）均在容器内运行而不影响宿主机；通过挂载在 /shared 的 shared_dir 目录在 agent 与宿主机之间交换文件。支持配置镜像、命令超时、资源限制、出站网络开关与额外 docker run 参数，容器在 Python 进程退出或上下文管理器块结束时自动停止并移除。要求宿主机装有 Docker，Python 3.12+；文档声明其适用于可信工作负载而非硬性多租户隔离。提供两个示例（pizza agent、sales analyst）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DockerSandbox 类为 Deep Agents 提供容器隔离的命令执行环境
- shared_dir 挂载目录实现 agent 与宿主机的文件交换
- 可配置容器镜像、命令超时、资源限制、出站网络与 docker run 参数
- 容器在进程退出（atexit）或上下文管理器块结束时自动停止并移除

## 适用场景

- 运行会执行任意 shell 命令的 Deep Agent 而不污染宿主机环境
- 需要 agent 与本地文件交互的数据分析工作流（如读写 CSV 与生成图表报告）
- 控制 agent 运行环境的网络访问与资源限额

## 场景标签

 · 领域:LLM Agent 基础设施

## 证据(README 行号)

> L9: Run Deep Agents in an isolated Docker container without compromising your host machine.
> L47: The creation of a `DockerSandbox` object results in the starting of a long-running docker container. Every shell co

## 星数曲线

```mermaid
xychart-beta
    title "andybbruno/deepagents-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8d99d92310da` · [字段定义](../../DATASET.md)*
