# francoisokada/llm-key-pool

⭐ 51 · C++ · MIT · 推送 2026-11-24 · [GitHub](https://github.com/francoisokada/llm-key-pool) · [官网](https://github.com/francoisokada/llm-key-pool/releases) · 个人维护

**为开发者轮换多家免费额度 LLM API key 的密钥池运行时**

面向 Windows 10/11 x64 的便携式 LLM API key 池工具：将用户持有的多个免费额度 key 聚合到单一端点，遇到 429 限流时自动轮换。提供免编译的预构建包与热重载 JSON 配置（改配置无需重启）、原子 JSON 状态与崩溃回滚、环形缓冲流水线与默认静默的 stderr 遥测。获取预构建包需输入访问码（2026）；也提供 CMake 源码构建路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多 provider 免费 key 池，429 自动轮换
- 热重载 JSON 配置，应用无需重启
- 原子 JSON 状态与崩溃安全回滚
- 提供 Windows x64 预构建包与源码构建

## 适用场景

- 聚合多个免费额度 API key 避免单 key 限流中断
- 为本地工具提供统一的 LLM API 端点
- 不改代码地调整 key 池配置（热重载）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3:  LLM Key Rotator — Multi-Provider API Key Pool with Automatic 429 Rotation (Hot-Reload Config, Zero Dependencies): O
> L18: **LLM Key Rotator — One endpoint, every free LLM key you own** (`llm-key-pool`) is a portable Windows 10/11 runtime


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `da68db76d432` · [字段定义](../../DATASET.md)*
