# alegrey91/vex8s

⭐ 41 · Go · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/alegrey91/vex8s) · 个人维护

**结合 Kubernetes 上下文判定 CVE 可利用性并生成 VEX 文档的扫描工具**

面向 Kubernetes 与供应链安全场景的命令行工具：读取容器漏洞报告（trivy/grype 生成）或主动调用二者引擎扫描，将 CVE 映射到 CWE 与利用类别，再解析 Kubernetes manifest 中的 securityContext 设置，判定 CVE 在当前工作负载配置下是否可利用；若被缓解则写入 VEX 文档，供后续扫描抑制告警。分类器默认为内嵌离线 ONNX 模型，也可选 Gemini 或本地 Ollama。项目自述为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CVE→CWE→利用类别的分类机制，内嵌离线 ONNX 模型无需网络
- 解析 manifest 中 securityContext 判定 CVE 是否可利用
- 被动/主动两种模式，支持 trivy 与 grype 引擎
- 可选 Gemini 或本地 Ollama 作为分类器

## 适用场景

- 降低容器扫描中的误报，抑制已被配置缓解的 CVE
- 为集群工作负载生成 VEX 文档供 trivy/grype 复用
- 在无网络环境用内嵌模型离线分类漏洞

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L19: * CVE description is processed by an embedded ML model to predict its *exploitation category*.
> L92: * **`embedded`** (default): an offline ONNX ML model

## 星数曲线

```mermaid
xychart-beta
    title "alegrey91/vex8s 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-29 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2be0bd9b1634` · [字段定义](../../DATASET.md)*
