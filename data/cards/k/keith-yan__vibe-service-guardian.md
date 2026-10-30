# keith-yan/vibe-service-guardian

⭐ 108 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/keith-yan/vibe-service-guardian) · 个人维护 · 中文 README

**本机开发服务溯源与本地 AI 运行时监控/容量规划工具**

面向 Windows/macOS/Linux 上 Vibe Coding 场景的本机工具：把监听端口的进程关联到项目、Agent/IDE/终端并判定是否疑似遗留；识别 Ollama、llama.cpp、vLLM 等推理运行时并做只读健康探测、基准校准与日志监控；读取本机硬件做开放权重模型容量规划与引擎兼容矩阵。控制台仅绑定 127.0.0.1，无云端遥测。当前为未签名 Alpha（v0.8.5.2-alpha.1），Windows 有验收证据，macOS/Linux 原生验收未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 端口监听进程→项目/Agent/终端的归属证据链与疑似遗留判定
- 对 Ollama、llama.cpp、vLLM、SGLang 等运行时的只读健康探测与固定负载基准
- 本机硬件读取→开放权重模型三种装载上限（物理/实际/SLA）的容量规划
- 归属纠正规则可审计、可回滚、跨机导入需重绑定

## 适用场景

- 开发机上排查哪个项目/Agent 留下了还在监听的服务
- 确认本机能否装载目标开放权重模型及支撑指定并发
- 监控本地模型服务的资源、OOM/加速器错误与运行健康

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: 0.8.5.1 优先解决四个日常高频问题：默认“今日关注”降低系统服务噪声；同一数据目录增加跨平台单实例锁；受保护/受管服务直接展示可执行但绝不代执行的建议路径；Ollama、llama.cpp、vLLM 原生只读适配器把当前模型
> L44: - 识别正在监听的 Ollama、llama.cpp/llamafile、vLLM、SGLang、MLX-LM、LM Studio、KTransformers、KoboldCpp、Hugging Face TGI、ComfyUI、
> L105: ## 模型容量规划闭环

## 星数曲线

```mermaid
xychart-beta
    title "keith-yan/vibe-service-guardian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 107 --> 110
    line [109, 108]
```

2026-10-18 109 → 2026-10-30 108（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `7c2b07dbcc18` · [字段定义](../../DATASET.md)*
