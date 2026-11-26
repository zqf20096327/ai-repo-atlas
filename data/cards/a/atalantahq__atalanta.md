# atalantahq/atalanta

⭐ 5 · Rust · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/atalantahq/atalanta) · [官网](https://atalanta.sh) · 组织维护

**YAML 编写移动/Web/API 测试的 Rust 单二进制测试运行器**

以单个 Rust 静态二进制运行 Android 模拟器、iOS 模拟器与 Chrome 上的测试套件，不依赖 JVM、Node 或 Appium 服务器。测试用 YAML 编写，也可由 AI agent 驱动应用生成（atalanta explore），生成结果经五次无模型重放与移位点击校验后才保存；保存后的测试在 CI 重放时不调用模型。支持同套件内的 HTTP API 步骤、失败时本地留存视频/日志/trace.html、跨设备并行与按历史时长分片。提供本地控制台与 MCP 服务器供 agent 操作设备。不支持 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制覆盖 Android/iOS/Chrome/API 四类目标，无 JVM/Node/Appium 依赖
- agent 生成测试经五次无模型重放与移位点击校验后才保存
- CI 重放不调用模型；支持并行、分片与受影响测试筛选
- MCP 服务器默认 5 个工具，--profile full 提供 33 个，覆盖主流编码 agent

## 适用场景

- 在 CI 中重放并行的移动端与 Web 端到端测试
- 让 AI agent 探索应用并生成 YAML 测试脚本
- 将 Maestro 流程迁移为本工具格式（atalanta migrate maestro）

## 场景标签

`浏览器自动化` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L14: Atalanta runs test suites on Android emulators, iOS simulators and Chrome. It is written in Rust: no JVM, no Node, 
> L27: - **No model in CI.** The model picks an operation and an element number; code builds every selector and fills ever
> L148: Only for `explore` and `do:` steps. Plain YAML tests need none. Local models work too: see AI providers.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0324887cccf1` · [字段定义](../../DATASET.md)*
